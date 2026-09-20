package com.example.ui.pages

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowForward
import androidx.compose.material.icons.filled.Bolt
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Lock
import androidx.compose.material.icons.filled.Public
import androidx.compose.material.icons.filled.VerifiedUser
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.model.Screen
import com.example.ui.components.AdSensePlaceholder

@Composable
fun HomeScreen(
  onNavigateToTool: (Screen) -> Unit,
  modifier: Modifier = Modifier
) {
  Column(
    modifier = modifier
      .fillMaxWidth()
      .padding(16.dp)
  ) {
    // Top Hero Header
    Column(
      modifier = Modifier
        .fillMaxWidth()
        .padding(vertical = 12.dp),
      horizontalAlignment = Alignment.CenterHorizontally
    ) {
      Box(
        modifier = Modifier
          .clip(RoundedCornerShape(20.dp))
          .background(MaterialTheme.colorScheme.primary.copy(alpha = 0.12f))
          .padding(horizontal = 14.dp, vertical = 6.dp)
      ) {
        Text(
          text = "100% FREE UTILITY PORTAL",
          style = MaterialTheme.typography.labelMedium,
          fontWeight = FontWeight.Bold,
          color = MaterialTheme.colorScheme.primary,
          letterSpacing = 1.sp
        )
      }

      Spacer(modifier = Modifier.height(12.dp))

      Text(
        text = "MY USEFUL TOOLS",
        style = MaterialTheme.typography.headlineLarge,
        fontWeight = FontWeight.Black,
        color = MaterialTheme.colorScheme.onBackground,
        textAlign = TextAlign.Center,
        letterSpacing = 0.5.sp
      )

      Spacer(modifier = Modifier.height(8.dp))

      Text(
        text = "Free, simple and easy-to-use online calculators and tools.",
        style = MaterialTheme.typography.bodyLarge,
        color = MaterialTheme.colorScheme.onSurfaceVariant,
        textAlign = TextAlign.Center,
        modifier = Modifier.padding(horizontal = 8.dp)
      )
    }

    // ADSENSE AREA 1: Near top of homepage
    AdSensePlaceholder(
      slotLabel = "AdSense Top Leaderboard (320x50 Mobile / 728x90 Desktop)",
      height = 75.dp
    )

    Spacer(modifier = Modifier.height(8.dp))

    // SECTION HEADING
    Row(
      modifier = Modifier.fillMaxWidth(),
      horizontalArrangement = Arrangement.SpaceBetween,
      verticalAlignment = Alignment.CenterVertically
    ) {
      Text(
        text = "Online Calculators",
        style = MaterialTheme.typography.titleLarge,
        fontWeight = FontWeight.Bold,
        color = MaterialTheme.colorScheme.onBackground
      )
      Text(
        text = "5 Free Tools",
        style = MaterialTheme.typography.labelMedium,
        color = MaterialTheme.colorScheme.primary,
        fontWeight = FontWeight.SemiBold
      )
    }

    Spacer(modifier = Modifier.height(12.dp))

    // 5 TOOL CARDS
    Screen.allTools.forEach { tool ->
      ToolCardItem(
        tool = tool,
        onOpenTool = { onNavigateToTool(tool) }
      )
      Spacer(modifier = Modifier.height(12.dp))
    }

    // ADSENSE AREA 2: Between content sections
    AdSensePlaceholder(
      slotLabel = "AdSense In-Feed Responsive Unit (300x250 Medium Rectangle)",
      height = 100.dp
    )

    Spacer(modifier = Modifier.height(8.dp))

    // WHY CHOOSE US / VALUE PROPOSITION SECTION
    Card(
      modifier = Modifier.fillMaxWidth(),
      colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
      shape = RoundedCornerShape(16.dp),
      elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
    ) {
      Column(modifier = Modifier.padding(18.dp)) {
        Text(
          text = "Why Use MY USEFUL TOOLS?",
          style = MaterialTheme.typography.titleMedium,
          fontWeight = FontWeight.Bold,
          color = MaterialTheme.colorScheme.onSurface
        )

        Spacer(modifier = Modifier.height(12.dp))

        FeatureHighlightRow(
          icon = Icons.Default.Bolt,
          title = "Instant & Client-Side",
          description = "Calculations evaluate instantly in your browser without waiting for server responses."
        )

        Spacer(modifier = Modifier.height(12.dp))

        FeatureHighlightRow(
          icon = Icons.Default.Lock,
          title = "100% Private & Secure",
          description = "No databases, no tracking cookies, and no account logins required."
        )

        Spacer(modifier = Modifier.height(12.dp))

        FeatureHighlightRow(
          icon = Icons.Default.VerifiedUser,
          title = "Completely Free",
          description = "No subscriptions, paywalls, or hidden charges. Free for everyone."
        )
      }
    }

    // ADSENSE AREA 3: Near bottom of homepage
    AdSensePlaceholder(
      slotLabel = "AdSense Bottom Anchor Banner (320x100 Large Mobile Banner)",
      height = 80.dp
    )
  }
}

@Composable
private fun ToolCardItem(
  tool: Screen,
  onOpenTool: () -> Unit
) {
  Card(
    modifier = Modifier
      .fillMaxWidth()
      .testTag("tool_card_${tool.route}"),
    colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
    shape = RoundedCornerShape(16.dp),
    elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
  ) {
    Column(modifier = Modifier.padding(18.dp)) {
      Row(
        verticalAlignment = Alignment.CenterVertically,
        modifier = Modifier.fillMaxWidth()
      ) {
        Box(
          modifier = Modifier
            .size(46.dp)
            .clip(RoundedCornerShape(12.dp))
            .background(MaterialTheme.colorScheme.primaryContainer),
          contentAlignment = Alignment.Center
        ) {
          Icon(
            imageVector = tool.icon,
            contentDescription = null,
            tint = MaterialTheme.colorScheme.primary,
            modifier = Modifier.size(26.dp)
          )
        }

        Spacer(modifier = Modifier.width(14.dp))

        Column(modifier = Modifier.weight(1f)) {
          Text(
            text = tool.title,
            style = MaterialTheme.typography.titleMedium,
            fontWeight = FontWeight.Bold,
            color = MaterialTheme.colorScheme.onSurface
          )
          Text(
            text = tool.metaTitle.substringBefore(" |"),
            style = MaterialTheme.typography.labelSmall,
            color = MaterialTheme.colorScheme.primary,
            fontWeight = FontWeight.Medium
          )
        }
      }

      Spacer(modifier = Modifier.height(10.dp))

      Text(
        text = tool.metaDescription,
        style = MaterialTheme.typography.bodyMedium,
        color = MaterialTheme.colorScheme.onSurfaceVariant,
        lineHeight = 20.sp
      )

      Spacer(modifier = Modifier.height(14.dp))

      // OPEN TOOL Button
      Button(
        onClick = onOpenTool,
        modifier = Modifier
          .fillMaxWidth()
          .height(48.dp)
          .testTag("open_tool_${tool.route}"),
        colors = ButtonDefaults.buttonColors(
          containerColor = MaterialTheme.colorScheme.primary
        ),
        shape = RoundedCornerShape(10.dp)
      ) {
        Text(
          text = "OPEN TOOL",
          fontWeight = FontWeight.Bold,
          letterSpacing = 0.5.sp
        )
        Spacer(modifier = Modifier.width(8.dp))
        Icon(
          imageVector = Icons.AutoMirrored.Filled.ArrowForward,
          contentDescription = null,
          modifier = Modifier.size(18.dp)
        )
      }
    }
  }
}

@Composable
private fun FeatureHighlightRow(
  icon: ImageVector,
  title: String,
  description: String
) {
  Row(
    verticalAlignment = Alignment.Top,
    modifier = Modifier.fillMaxWidth()
  ) {
    Box(
      modifier = Modifier
        .size(36.dp)
        .clip(CircleShape)
        .background(MaterialTheme.colorScheme.primary.copy(alpha = 0.1f)),
      contentAlignment = Alignment.Center
    ) {
      Icon(
        imageVector = icon,
        contentDescription = null,
        tint = MaterialTheme.colorScheme.primary,
        modifier = Modifier.size(20.dp)
      )
    }

    Spacer(modifier = Modifier.width(12.dp))

    Column(modifier = Modifier.weight(1f)) {
      Text(
        text = title,
        style = MaterialTheme.typography.bodyMedium,
        fontWeight = FontWeight.Bold,
        color = MaterialTheme.colorScheme.onSurface
      )
      Text(
        text = description,
        style = MaterialTheme.typography.bodySmall,
        color = MaterialTheme.colorScheme.onSurfaceVariant
      )
    }
  }
}
