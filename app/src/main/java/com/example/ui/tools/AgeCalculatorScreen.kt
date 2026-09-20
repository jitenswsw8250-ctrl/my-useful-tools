package com.example.ui.tools

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Cake
import androidx.compose.material.icons.filled.CalendarMonth
import androidx.compose.material.icons.filled.Clear
import androidx.compose.material.icons.filled.Event
import androidx.compose.material.icons.filled.Schedule
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.DatePicker
import androidx.compose.material3.DatePickerDialog
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.rememberDatePickerState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.ui.components.AdSensePlaceholder
import java.text.SimpleDateFormat
import java.util.Calendar
import java.util.Locale

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AgeCalculatorScreen(modifier: Modifier = Modifier) {
  var birthDay by rememberSaveable { mutableStateOf("15") }
  var birthMonth by rememberSaveable { mutableStateOf("6") }
  var birthYear by rememberSaveable { mutableStateOf("1995") }

  var calculationResult by remember {
    mutableStateOf<AgeResult?>(calculateAge(15, 6, 1995))
  }
  var errorMessage by remember { mutableStateOf<String?>(null) }
  var showDatePicker by remember { mutableStateOf(false) }

  val datePickerState = rememberDatePickerState()

  Column(
    modifier = modifier
      .fillMaxWidth()
      .padding(16.dp)
  ) {
    // Page Heading & SEO Friendly Context
    Text(
      text = "Age Calculator",
      style = MaterialTheme.typography.headlineMedium,
      fontWeight = FontWeight.Bold,
      color = MaterialTheme.colorScheme.onBackground
    )
    Text(
      text = "Calculate your exact age in years, months, and days, and find out how long until your next birthday.",
      style = MaterialTheme.typography.bodyMedium,
      color = MaterialTheme.colorScheme.onSurfaceVariant,
      modifier = Modifier.padding(top = 4.dp, bottom = 12.dp)
    )

    // AdSense Placement Top of Tool
    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - Age Tool Top")

    // Input Card
    Card(
      modifier = Modifier
        .fillMaxWidth()
        .padding(vertical = 8.dp),
      colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
      elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
      shape = RoundedCornerShape(16.dp)
    ) {
      Column(modifier = Modifier.padding(16.dp)) {
        Row(
          modifier = Modifier.fillMaxWidth(),
          horizontalArrangement = Arrangement.SpaceBetween,
          verticalAlignment = Alignment.CenterVertically
        ) {
          Text(
            text = "Enter Date of Birth",
            style = MaterialTheme.typography.titleMedium,
            fontWeight = FontWeight.SemiBold
          )

          OutlinedButton(
            onClick = { showDatePicker = true },
            modifier = Modifier.testTag("open_calendar_picker")
          ) {
            Icon(
              imageVector = Icons.Default.CalendarMonth,
              contentDescription = "Open Calendar",
              modifier = Modifier.size(18.dp)
            )
            Spacer(modifier = Modifier.width(6.dp))
            Text("Pick Date")
          }
        }

        Spacer(modifier = Modifier.height(16.dp))

        // Quick Input Fields (Day, Month, Year)
        Row(
          modifier = Modifier.fillMaxWidth(),
          horizontalArrangement = Arrangement.spacedBy(8.dp)
        ) {
          OutlinedTextField(
            value = birthDay,
            onValueChange = { if (it.length <= 2) birthDay = it },
            label = { Text("Day") },
            placeholder = { Text("DD") },
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            singleLine = true,
            modifier = Modifier
              .weight(1f)
              .testTag("birth_day_input")
          )

          OutlinedTextField(
            value = birthMonth,
            onValueChange = { if (it.length <= 2) birthMonth = it },
            label = { Text("Month") },
            placeholder = { Text("MM") },
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            singleLine = true,
            modifier = Modifier
              .weight(1f)
              .testTag("birth_month_input")
          )

          OutlinedTextField(
            value = birthYear,
            onValueChange = { if (it.length <= 4) birthYear = it },
            label = { Text("Year") },
            placeholder = { Text("YYYY") },
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            singleLine = true,
            modifier = Modifier
              .weight(1.3f)
              .testTag("birth_year_input")
          )
        }

        if (errorMessage != null) {
          Spacer(modifier = Modifier.height(8.dp))
          Text(
            text = errorMessage ?: "",
            color = MaterialTheme.colorScheme.error,
            style = MaterialTheme.typography.bodySmall
          )
        }

        Spacer(modifier = Modifier.height(16.dp))

        // Action Buttons: Calculate & Clear
        Row(
          modifier = Modifier.fillMaxWidth(),
          horizontalArrangement = Arrangement.spacedBy(12.dp)
        ) {
          Button(
            onClick = {
              val d = birthDay.toIntOrNull()
              val m = birthMonth.toIntOrNull()
              val y = birthYear.toIntOrNull()

              if (d == null || m == null || y == null || d !in 1..31 || m !in 1..12 || y !in 1900..2100) {
                errorMessage = "Please enter a valid date (Day 1-31, Month 1-12, Year 1900-present)."
                calculationResult = null
              } else {
                val res = calculateAge(d, m, y)
                if (res == null) {
                  errorMessage = "Date cannot be in the future."
                  calculationResult = null
                } else {
                  errorMessage = null
                  calculationResult = res
                }
              }
            },
            modifier = Modifier
              .weight(1f)
              .height(48.dp)
              .testTag("calculate_age_button")
          ) {
            Icon(imageVector = Icons.Default.Event, contentDescription = null, modifier = Modifier.size(18.dp))
            Spacer(modifier = Modifier.width(6.dp))
            Text("Calculate Age")
          }

          OutlinedButton(
            onClick = {
              birthDay = ""
              birthMonth = ""
              birthYear = ""
              calculationResult = null
              errorMessage = null
            },
            modifier = Modifier
              .height(48.dp)
              .testTag("clear_age_button")
          ) {
            Icon(imageVector = Icons.Default.Clear, contentDescription = null, modifier = Modifier.size(18.dp))
            Spacer(modifier = Modifier.width(6.dp))
            Text("Clear")
          }
        }
      }
    }

    // DatePicker Dialog
    if (showDatePicker) {
      DatePickerDialog(
        onDismissRequest = { showDatePicker = false },
        confirmButton = {
          TextButton(
            onClick = {
              datePickerState.selectedDateMillis?.let { millis ->
                val cal = Calendar.getInstance().apply { timeInMillis = millis }
                birthDay = cal.get(Calendar.DAY_OF_MONTH).toString()
                birthMonth = (cal.get(Calendar.MONTH) + 1).toString()
                birthYear = cal.get(Calendar.YEAR).toString()
                calculationResult = calculateAge(
                  cal.get(Calendar.DAY_OF_MONTH),
                  cal.get(Calendar.MONTH) + 1,
                  cal.get(Calendar.YEAR)
                )
                errorMessage = null
              }
              showDatePicker = false
            }
          ) {
            Text("Select")
          }
        },
        dismissButton = {
          TextButton(onClick = { showDatePicker = false }) {
            Text("Cancel")
          }
        }
      ) {
        DatePicker(state = datePickerState)
      }
    }

    // Results Display
    calculationResult?.let { result ->
      Spacer(modifier = Modifier.height(16.dp))

      Card(
        modifier = Modifier
          .fillMaxWidth()
          .testTag("age_result_card"),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.primaryContainer),
        shape = RoundedCornerShape(16.dp)
      ) {
        Column(
          modifier = Modifier.padding(20.dp),
          horizontalAlignment = Alignment.CenterHorizontally
        ) {
          Text(
            text = "YOUR EXACT AGE",
            style = MaterialTheme.typography.labelMedium,
            fontWeight = FontWeight.Bold,
            color = MaterialTheme.colorScheme.onPrimaryContainer.copy(alpha = 0.8f),
            letterSpacing = 1.2.sp
          )

          Spacer(modifier = Modifier.height(12.dp))

          // Years, Months, Days Highlights
          Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceEvenly
          ) {
            AgeMetricBox(value = result.years.toString(), label = "Years")
            AgeMetricBox(value = result.months.toString(), label = "Months")
            AgeMetricBox(value = result.days.toString(), label = "Days")
          }

          Spacer(modifier = Modifier.height(16.dp))

          // Next Birthday Highlight
          Box(
            modifier = Modifier
              .fillMaxWidth()
              .clip(RoundedCornerShape(12.dp))
              .background(MaterialTheme.colorScheme.surface)
              .padding(14.dp)
          ) {
            Row(
              verticalAlignment = Alignment.CenterVertically,
              modifier = Modifier.fillMaxWidth()
            ) {
              Icon(
                imageVector = Icons.Default.Cake,
                contentDescription = null,
                tint = MaterialTheme.colorScheme.primary,
                modifier = Modifier.size(32.dp)
              )
              Spacer(modifier = Modifier.width(12.dp))
              Column {
                Text(
                  text = "Next Birthday",
                  style = MaterialTheme.typography.titleSmall,
                  fontWeight = FontWeight.Bold,
                  color = MaterialTheme.colorScheme.onSurface
                )
                Text(
                  text = "${result.monthsUntilNextBirthday} months, ${result.daysUntilNextBirthday} days remaining",
                  style = MaterialTheme.typography.bodyMedium,
                  color = MaterialTheme.colorScheme.onSurfaceVariant
                )
                Text(
                  text = "Day: ${result.nextBirthdayDayOfWeek}",
                  style = MaterialTheme.typography.bodySmall,
                  color = MaterialTheme.colorScheme.primary,
                  fontWeight = FontWeight.Medium
                )
              }
            }
          }

          Spacer(modifier = Modifier.height(12.dp))

          // Detailed statistics
          Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(8.dp)
          ) {
            StatPill(
              title = "Total Days",
              value = "%,d".format(result.totalDays),
              modifier = Modifier.weight(1f)
            )
            StatPill(
              title = "Total Hours",
              value = "%,d".format(result.totalHours),
              modifier = Modifier.weight(1f)
            )
            StatPill(
              title = "Zodiac Sign",
              value = result.zodiacSign,
              modifier = Modifier.weight(1f)
            )
          }
        }
      }
    }

    Spacer(modifier = Modifier.height(16.dp))
    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - Age Tool Bottom")
  }
}

@Composable
private fun AgeMetricBox(value: String, label: String) {
  Column(
    horizontalAlignment = Alignment.CenterHorizontally,
    modifier = Modifier
      .clip(RoundedCornerShape(12.dp))
      .background(MaterialTheme.colorScheme.surface)
      .padding(horizontal = 16.dp, vertical = 12.dp)
  ) {
    Text(
      text = value,
      style = MaterialTheme.typography.headlineMedium,
      fontWeight = FontWeight.Black,
      color = MaterialTheme.colorScheme.primary
    )
    Text(
      text = label,
      style = MaterialTheme.typography.labelSmall,
      color = MaterialTheme.colorScheme.onSurfaceVariant
    )
  }
}

@Composable
private fun StatPill(title: String, value: String, modifier: Modifier = Modifier) {
  Column(
    modifier = modifier
      .clip(RoundedCornerShape(8.dp))
      .background(MaterialTheme.colorScheme.surface.copy(alpha = 0.7f))
      .padding(8.dp),
    horizontalAlignment = Alignment.CenterHorizontally
  ) {
    Text(
      text = title,
      style = MaterialTheme.typography.labelSmall,
      color = MaterialTheme.colorScheme.onSurfaceVariant,
      fontSize = 10.sp
    )
    Text(
      text = value,
      style = MaterialTheme.typography.bodyMedium,
      fontWeight = FontWeight.Bold,
      color = MaterialTheme.colorScheme.onSurface
    )
  }
}

data class AgeResult(
  val years: Int,
  val months: Int,
  val days: Int,
  val monthsUntilNextBirthday: Int,
  val daysUntilNextBirthday: Int,
  val nextBirthdayDayOfWeek: String,
  val totalDays: Long,
  val totalHours: Long,
  val zodiacSign: String
)

private fun calculateAge(day: Int, month: Int, year: Int): AgeResult? {
  val today = Calendar.getInstance()
  val birth = Calendar.getInstance().apply {
    set(Calendar.YEAR, year)
    set(Calendar.MONTH, month - 1)
    set(Calendar.DAY_OF_MONTH, day)
    set(Calendar.HOUR_OF_DAY, 0)
    set(Calendar.MINUTE, 0)
    set(Calendar.SECOND, 0)
    set(Calendar.MILLISECOND, 0)
  }

  if (birth.after(today)) return null

  var years = today.get(Calendar.YEAR) - birth.get(Calendar.YEAR)
  var months = today.get(Calendar.MONTH) - birth.get(Calendar.MONTH)
  var days = today.get(Calendar.DAY_OF_MONTH) - birth.get(Calendar.DAY_OF_MONTH)

  if (days < 0) {
    months -= 1
    val prevMonth = (today.clone() as Calendar).apply { add(Calendar.MONTH, -1) }
    days += prevMonth.getActualMaximum(Calendar.DAY_OF_MONTH)
  }

  if (months < 0) {
    years -= 1
    months += 12
  }

  // Next birthday calculation
  val nextBday = Calendar.getInstance().apply {
    set(Calendar.MONTH, month - 1)
    set(Calendar.DAY_OF_MONTH, day)
    set(Calendar.HOUR_OF_DAY, 0)
    set(Calendar.MINUTE, 0)
    set(Calendar.SECOND, 0)
    set(Calendar.MILLISECOND, 0)
    set(Calendar.YEAR, today.get(Calendar.YEAR))
  }

  if (nextBday.before(today)) {
    nextBday.add(Calendar.YEAR, 1)
  }

  var nextMonths = nextBday.get(Calendar.MONTH) - today.get(Calendar.MONTH)
  var nextDays = nextBday.get(Calendar.DAY_OF_MONTH) - today.get(Calendar.DAY_OF_MONTH)

  if (nextDays < 0) {
    nextMonths -= 1
    val tempCal = (today.clone() as Calendar)
    nextDays += tempCal.getActualMaximum(Calendar.DAY_OF_MONTH)
  }
  if (nextMonths < 0) {
    nextMonths += 12
  }

  val dayOfWeekFormat = SimpleDateFormat("EEEE", Locale.getDefault())
  val nextBdayDayOfWeek = dayOfWeekFormat.format(nextBday.time)

  val diffMillis = today.timeInMillis - birth.timeInMillis
  val totalDays = diffMillis / (1000 * 60 * 60 * 24)
  val totalHours = totalDays * 24

  val zodiac = getZodiacSign(day, month)

  return AgeResult(
    years = years,
    months = months,
    days = days,
    monthsUntilNextBirthday = nextMonths,
    daysUntilNextBirthday = nextDays,
    nextBirthdayDayOfWeek = nextBdayDayOfWeek,
    totalDays = totalDays,
    totalHours = totalHours,
    zodiacSign = zodiac
  )
}

private fun getZodiacSign(day: Int, month: Int): String {
  return when (month) {
    1 -> if (day < 20) "Capricorn ♑" else "Aquarius ♒"
    2 -> if (day < 19) "Aquarius ♒" else "Pisces ♓"
    3 -> if (day < 21) "Pisces ♓" else "Aries ♈"
    4 -> if (day < 20) "Aries ♈" else "Taurus ♉"
    5 -> if (day < 21) "Taurus ♉" else "Gemini ♊"
    6 -> if (day < 21) "Gemini ♊" else "Cancer ♋"
    7 -> if (day < 23) "Cancer ♋" else "Leo ♌"
    8 -> if (day < 23) "Leo ♌" else "Virgo ♍"
    9 -> if (day < 23) "Virgo ♍" else "Libra ♎"
    10 -> if (day < 23) "Libra ♎" else "Scorpio ♏"
    11 -> if (day < 22) "Scorpio ♏" else "Sagittarius ♐"
    12 -> if (day < 22) "Sagittarius ♐" else "Capricorn ♑"
    else -> "Aries ♈"
  }
}
